# **Effective Python**

> - Know the Python version
```Python
import sys

print(sys.version)
```

> - The Zen of Python
    * There should be one-and preferably only one-obvious way to do it.
```Python
import this
```

> - Follow PEP8
> - Know the difference between str and bytes.
    * Bytes instances contain raw, unsigned 8-bit values.

> - Using generator instead of lists. Know what is generator in Python and how to use a generator.
Generator can produce a sequence of outputs for arbitarily large input because their working memory does not include all inputs and outputs.

> - 37: Compose classes instead of nesting many levels of builtin-types
```python
from collections import defaultdict
'''
Record the grades of a set of students whose names are not known in advance.
'''
class GradeBook:
    def __init__(self):
        self._grades = {}

    def add_students(self, name: str) -> None:
        self._grades[name] = []
    
    def report_grade(self, name, score) -> None:
        self._grades[name].append(score)

    def average_grade(self, name) -> float:
        grades = self._grades[name]
        return sum(grades)/len(grades)

'''
Extend the grade book example above so it keep a list of grades by subject
'''
class GradeBySubject:
    def __init(self):
        self._grades = {}
    
    def add_student(self, name):
        self._grades[name] = defaultdict(list)
    
    def report_grade(self, name: str, subject: str, score: Union[int, float]) -> None:
        self._grades[name][subject].append(score)

    def average_grade(self, name) -> float:
        by_subject = self._grades[name]
        total, count = 0, 0
        for grades in by_subject.values():
            total += sum(grades)
            count += len(grades)
        return total / count

'''
The requirements change again, track the weight of each score toward the overall grade in the class so that the midterm and final exams are more important than pop quizzes.
'''
class WeightedGradebook:
    def __init__(self):
        self._grades = {}

    def add_student(self, name: str) -> None:
        self._grades[name] = defaultdict(list)

    def report_grade(self, name: str, subject: str, score: Union[int, float], weight: Union[int, float]):
        by_subject = self._grades[name]
        grade_list = by_subject[subject]
        grade_list.append((score, weight))

    def average_grade(self, name: str) -> float:
        by_subject = self._grades[name]
        score_sum, score_count = 0, 0
        for subject, scores in by_subject.items():
            subject_avg, total_weight = 0, 0
            for score, weight in scores:
                subject_avg += score * weight
                total_weight += weight
            score_sum += subject_avg / total_weight
            score_count += 1
        return score_sum / score_count

'''
The code above can be complex, the bookkeeping of grade is getting complicated. And sometimes OOP class can be too heavyweightt for this sort of task
'''
```
    * Avoid making dictionaries with values that are dictionaries, long tuples, or complex nestings of other built-in types
    * Use namedtuple for lightweight, immutable data containers before you need the flexibility of a full class.
    * Move the code to using multiple classes when the internal state dictionaries get complicated.

> - 38: Accept functions instead of classes for simple interfaces