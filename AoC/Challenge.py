import logging as _logging
import os as _os
import time as _time

from .getInput import getInput as _getInput
from .misc import copy as _copy

class Challenge():

    def __init__(self, year, day):
        self.year = year
        self.day = day


    _testCases = {}
    def addTestCase(self, testInputFile, part1, part2, extension = False):
        name = ".".join(testInputFile.split(".")[:-1])

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
            "isExtension": extension,
        }


    def _validateTestCase(self, testCase):

        testCase = self._testCases[testCase]
        passed = 0
        total = 0

        result, time = (None, 0) if testCase["part1"] is None else self._executePart1(testCase["input"])
        time = round(time, 4)
        if result is not None:
            total += 1
            if testCase["part1"] == result:
                _logging.info(f"Passed {testCase['name']} part 1, took {time}s.")
                passed += 1
            else:
                _logging.error(f"Failed {testCase['name']} part 1. Expected {testCase['part1']}, but received {result}. Took {time}s.")
        else:
            if testCase["part1"] is None:
                _logging.info(f"{testCase['name']} part 1 is None. Skipping.")
            else:
                _logging.info(f"Part 1 return value is None. Skipping.")

        result, time = (None, 0) if testCase["part2"] is None else self._executePart2(testCase["input"])
        time = round(time, 4)
        if result is not None:
            total += 1
            if testCase["part2"] == result:
                _logging.info(f"Passed {testCase['name']} part 2, took {time}s.")
                passed += 1
            else:
                _logging.error(f"Failed {testCase['name']} part 2. Expected {testCase['part2']}, but received {result}. Took {time}s.")
        else:
            if testCase["part2"] is None:
                _logging.info(f"{testCase['name']} part 2 is None. Skipping.")
            else:
                _logging.info(f"Part 2 return value is None. Skipping.")

        return (passed, total)

    def _validateChallenge(self, extensions = False):

        passedTests = 0
        totalTests = 0
        for testCase in self._testCases:
            if self._testCases[testCase]["isExtension"] is not extensions: continue
            passed, total = self._validateTestCase(testCase)
            passedTests += passed
            totalTests += total

        if passedTests == totalTests:
            _logging.info(f"Passed all [{passedTests}/{totalTests}] {'extensions' if extensions else 'tests'}.")
        else:
            _logging.error(f"Passed [{passedTests}/{totalTests}] {'extensions.' if extensions else 'tests, final result may be incorrect.'}")


    def runChallenge(self, inputFile, extensionDelay = 5):

        _logging.info("Validating challenge with test cases.")
        self._validateChallenge()

        try:
            with open(inputFile) as f:
                data = f.read()
        except FileNotFoundError:
            _logging.info("Input file not found, retrieving from adventofcode.com.")
            data = _getInput(self.year, self.day)
            with open(inputFile, "w") as f:
                f.write(data)

        part1, time = self._executePart1(data)
        time = round(time, 4)
        _logging.info(f"Part 1 result: {part1}, took {time}s.")
        part2, time = self._executePart2(data)
        time = round(time, 4)
        _logging.info(f"Part 2 result: {part2}, took {time}s.")

        if part2 is None and part1 is not None:
            _logging.info("Only part 1 returned a value, copying it to the clipboard.")
            _copy(part1)
        elif part1 is None and part2 is not None:
            _logging.info("Only part 2 returned a value, copying it to the clipboard.")
            _copy(part2)

        _time.sleep(extensionDelay)
        _logging.info("Testing challenge with extension cases.")
        self._validateChallenge(extensions = True)

    def _executePart1(self, data):
        t0 = _time.time()
        result = self.part1(self.parse1(data))
        t1 = _time.time()
        return (result, t1-t0)
    def _executePart2(self, data):
        t0 = _time.time()
        result = self.part2(self.parse2(data))
        t1 = _time.time()
        return (result, t1-t0)


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