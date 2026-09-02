# Wikipedia fetcher — primary data source

import re

import requests

from fetchers.base_fetcher import BaseFetcher

API_URL = "https://en.wikipedia.org/w/api.php"
USER_AGENT = "What-the-Izm/1.0 (Primo English curriculum program; contact: educational use)"
TIMEOUT = 15

STRIP_SECTIONS = [
    "References", "External links", "See also", "Bibliography",
    "Further reading", "Notes", "Citations", "Footnotes"
]


class WikipediaFetcher(BaseFetcher):

    def fetch(self, theory_name: str, stage: int, location: str = None) -> dict:
        try:
            title = theory_name.strip().capitalize()
            text = self._fetch_page_text(title)
            if text is None:
                print(f"[WikipediaFetcher] Warning: no content found for '{title}'")
                return self._empty_result(theory_name, stage, location)

            summary_text = self._strip_sections(text)

            if location:
                location_title = f"{theory_name.strip().capitalize()} in {location.strip().title()}"
                location_text = self._fetch_page_text(location_title)
                if location_text is not None:
                    location_text = self._strip_sections(location_text)
                    summary_text += f"\n\n--- Source: Wikipedia ({location}) ---\n\n{location_text}"
                else:
                    print(f"[WikipediaFetcher] Warning: no content found for '{location_title}'")

            word_count = len(summary_text.split())

            result = self._empty_result(theory_name, stage, location)
            result["word_count"] = word_count
            result["summary_text"] = summary_text
            return result

        except requests.exceptions.RequestException as e:
            print(f"[WikipediaFetcher] Warning: HTTP error or timeout — {e}")
            return self._empty_result(theory_name, stage, location)
        except Exception as e:
            print(f"[WikipediaFetcher] Warning: unexpected exception — {e}")
            return self._empty_result(theory_name, stage, location)

    def _fetch_page_text(self, title: str) -> str:
        params = {
            "action": "query",
            "prop": "extracts",
            "explaintext": "true",
            "redirects": "true",
            "titles": title,
            "format": "json",
        }
        headers = {"User-Agent": USER_AGENT}

        response = requests.get(API_URL, params=params, headers=headers, timeout=TIMEOUT)
        response.raise_for_status()
        data = response.json()

        pages = data.get("query", {}).get("pages", {})
        if not pages:
            return None

        page = next(iter(pages.values()))
        if "missing" in page:
            return None

        extract = page.get("extract", "")
        if not extract:
            return None

        return extract

    def _strip_sections(self, text: str) -> str:
        pattern = r'\n==[^=].*?==\n'
        parts = re.split(pattern, text)
        headers = re.findall(pattern, text)

        result = [parts[0]]
        for header, part in zip(headers, parts[1:]):
            header_text = header.strip().strip('=').strip()
            if header_text not in STRIP_SECTIONS:
                result.append(header)
                result.append(part)
        return ''.join(result)
