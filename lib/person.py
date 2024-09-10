class Person:
    approved_jobs = ["Admin", "Customer Service", "Human Resources", "ITC", "Production"]

    def __init__(self, name="John Doe", job="Admin"):
        # Initialize the name, the job will only be set if the name is valid
        self._name = None
        self._job = None
        self.name = name
        if self._name is not None:  # Only set job if name is valid
            self.job = job

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value.title()  # Convert to title case
        else:
            self._name = None  # Reset name to None if invalid
            print("Name must be string between 1 and 25 characters.")

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if value in Person.approved_jobs:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
