import csv
from Calculator import Calculator

class CSVCalculatorHandler:
    def __init__(self):
        self.calc = Calculator()
        self.history = []

    def process_csv(self, filenames, output_prefix="output"):
        for i, filename in enumerate(filenames):
            with open(filename, newline='') as f_in, open(f"{output_prefix}_{i}.csv", "w", newline='') as f_out:
                read = csv.reader(f_in)
                writer = csv.writer(f_out)
                writer.writerow(["result", "error"])

                for row in read:
                    *nums, op = row
                    nums = [float(x) for x in nums]

                    result, error = None, 0
                    if op == "add" and len(nums) >= 2:
                        result = self.calc.add(*nums)
                    elif op == "subtract" and len(nums) >= 2:
                        result = self.calc.subtract(*nums)
                    elif op == "multiply" and len(nums) >= 2:
                        result = self.calc.multiply(*nums)
                    elif op == "divide" and len(nums) == 2:
                        if nums[1] == 0:
                            error = 1
                        else:
                            result = self.calc.divide(*nums)
                    elif op == "exponentiate" and len(nums) == 2:
                        result = self.calc.exponentiate(*nums)
                    elif len(nums) < 2:
                        error = 2
                    else:
                        error = 3

                    writer.writerow([result if result is not None else "", error])
                    self.save_to_history(filename, ",".join(row), result, error)

    def save_to_history(self, filename, operation, result, error_code):
        self.history.append([filename, operation, result if result is not None else "", error_code])

    def history_export(self, export_filename):
        with open(export_filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["input_file", "operation", "result", "error"])
            writer.writerows(self.history)