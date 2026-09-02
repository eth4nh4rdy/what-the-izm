# Abstract base fetcher — interface all fetchers must implement

from abc import ABC, abstractmethod


class BaseFetcher(ABC):

    @abstractmethod
    def fetch(self, theory_name: str, stage: int, location: str = None) -> dict:
        """
        Fetch content for the given theory and stage.
        Optional location narrows content to a geographic or cultural context.
        Returns a standardized content dict — see Phase 1 roadmap for schema.
        Never raises an exception on missing content — returns empty dict with word_count 0.
        """
        pass

    def _empty_result(self, theory_name: str, stage: int, location: str = None) -> dict:
        """
        Returns a valid empty result dict.
        Call this when content cannot be retrieved.
        """
        return {
            "source": self.__class__.__name__,
            "theory": theory_name,
            "stage": stage,
            "location": location,
            "word_count": 0,
            "summary_text": "",
            "key_figures": [],
            "key_texts": [],
            "controversies": [],
            "raw_text": ""
        }
