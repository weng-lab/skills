import unittest

from catalog import grouping_errors


class CatalogTests(unittest.TestCase):
    def test_valid_catalog_with_optional_fields_omitted(self):
        self.assertEqual(grouping_errors({"groupings": [{"title": "Writing", "skills": ["prose"]}]}, ["prose"]), [])

    def test_retired_and_missing_skills(self):
        errors = grouping_errors({"groupings": [{"title": "Writing", "skills": ["old"]}]}, ["new"])
        self.assertTrue(any("unknown source skill 'old'" in e for e in errors))
        self.assertTrue(any("ungrouped source skills ['new']" in e for e in errors))

    def test_duplicate_membership(self):
        config = {"groupings": [{"title": title, "skills": ["prose"]} for title in ["Writing", "Other"]]}
        self.assertTrue(any("appears more than once" in e for e in grouping_errors(config, ["prose"])))

    def test_malformed_configuration_is_reported(self):
        for config in [None, [], {}, {"groupings": [None]}, {"groupings": [{"title": [], "skills": [None]}]}, {"groupings": [{"title": "Empty", "skills": []}]}]:
            with self.subTest(config=config):
                self.assertTrue(grouping_errors(config, ["prose"]))

    def test_display_options_and_typos(self):
        config = {"notGrouped": "hidden", "groupings": [{"title": "Writing", "skills": ["prose"], "descripton": "Typo"}]}
        errors = grouping_errors(config, ["prose"])
        self.assertTrue(any("notGrouped" in e for e in errors))
        self.assertTrue(any("unknown fields" in e for e in errors))

    def test_service_limits(self):
        for config in [{"groupings": [{"title": str(i), "skills": [str(i)]} for i in range(51)]}, {"groupings": [{"title": "Too many", "skills": [str(i) for i in range(501)]}]}]:
            self.assertTrue(grouping_errors(config, []))


if __name__ == "__main__":
    unittest.main()
