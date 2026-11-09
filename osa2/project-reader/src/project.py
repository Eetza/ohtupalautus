class Project:
    def __init__(
        self, name, description, license_name, authors,
        dependencies, dev_dependencies
    ):
        self.name = name
        self.description = description
        self.license = license_name
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, items):
        return "\n".join(f"- {item}" for item in items) if items else "-"

    def __str__(self):
        return (
            f"Name: {self.name}"
            f"\nDescription: {self.description or '-'}"
            f"\nLicense: {self.license or '-'}"
            f"\n\nAuthors:\n{self._stringify_list(self.authors)}"
            f"\n\nDependencies:\n{self._stringify_list(self.dependencies)}"
            "\n\nDevelopment dependencies:"
            f"\n{self._stringify_list(self.dev_dependencies)}"
        )