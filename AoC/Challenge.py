import logging as _logging
import os as _os

from .getInput import getInput as _getInput
from .misc import copy as _copy

class Challenge():

    def __init__(self, year, day):
        self.year = year
        self.day = day


    _testCases = {}
    def addTestCase(self, testInputFile, part1, part2, name = None):
        if name is None: name = ".".join(testInputFile.split(".")[:-1])

        if testInputFile in self._testCases:
            raise ValueError(f"A test already exists with the name {testInputFile} in the challenge for {self.year}, day {self.day}.")

        with open(testInputFile) as f:
            data = f.read()

        self._testCases[name] = {
            "name": name,
            "fileName": testInputFile,
            "input": data,
            "part1": part1,
            "part2": part2,
        }


    def _validateTestCase(self, testCase):

        testCase = self._testCases[testCase]
        passed = 0
        total = 0

        part1 = None if testCase["part1"] is None else self._executePart1(testCase["input"])
        if part1 is not None:
            total += 1
            if testCase["part1"] == part1:
                _logging.info(f"Passed {testCase['name']} part 1.")
                passed += 1
            else:
                _logging.error(f"Failed {testCase['name']} part 1. Expected {testCase['part1']}, but received {part1}.")
        else:
            if testCase["part1"] is None:
                _logging.info(f"{testCase['name']} part 1 is None. Skipping.")
            else:
                _logging.info(f"Part 1 return value is None. Skipping.")

        part2 = None if testCase["part2"] is None else self._executePart2(testCase["input"])
        if part2 is not None:
            total += 1
            if testCase["part2"] == part2:
                _logging.info(f"Passed {testCase['name']} part 2.")
                passed += 1
            else:
                _logging.error(f"Failed {testCase['name']} part 2. Expected {testCase['part2']}, but received {part2}.")
        else:
            if testCase["part2"] is None:
                _logging.info(f"{testCase['name']} part 2 is None. Skipping.")
            else:
                _logging.info(f"Part 2 return value is None. Skipping.")

        return (passed, total)

    def _validateChallenge(self):

        passedTests = 0
        totalTests = 0
        for testCase in self._testCases:
            result = self._validateTestCase(testCase)
            passedTests += result[0]
            totalTests += result[1]

        if passedTests == totalTests:
            _logging.info(f"Passed all [{passedTests}/{totalTests}] tests.")
        else:
            _logging.error(f"Passed [{passedTests}/{totalTests}] tests, final result may be incorrect.")


    def runChallenge(self, inputFile):

        self._validateChallenge()

        try:
            with open(inputFile) as f:
                data = f.read()
        except FileNotFoundError:
            _logging.info("Input file not found, retrieving from adventofcode.com.")
            data = _getInput(self.year, self.day)
            with open(inputFile, "w") as f:
                f.write(data)

        part1 = self._executePart1(data)
        _logging.info(f"Part 1 result: {part1}")
        part2 = self._executePart2(data)
        _logging.info(f"Part 2 result: {part2}")

        if part2 is None and part1 is not None:
            _logging.info("Only part 1 returned a value, copying it to the clipboard.")
            _copy(part1)
        elif part1 is None and part2 is not None:
            _logging.info("Only part 2 returned a value, copying it to the clipboard.")
            _copy(part2)

    def _executePart1(self, data):
        return self.part1(self.parse1(data))
    def _executePart2(self, data):
        return self.part2(self.parse2(data))


    def execute(self, data):
        return None
    def part1(self, data):
        return self.execute(data)
    def part2(self, data):
        return self.execute(data)

    def parse(self, data):
        return data
    def parse1(self, data):
        return self.parse(data)
    def parse2(self, data):
        return self.parse(data)