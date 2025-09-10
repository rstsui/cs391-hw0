import csv
from Calculator import Calculator

class CSVCalculatorHandler:
    def __init__(self):
        # create calculator object
        self.calc = Calculator()
        #store history
        self.history = []

    def process_csv(self, filenames, output_prefix="output"):
        for i, filename in enumerate(filenames):
            with open(filename, newline='') as f_in, open(f"{output_prefix}_{i}.csv", "w", newline='') as f_out:
                #read the file 
                read = csv.reader(f_in)
                #write header row
                writer = csv.writer(f_out)
                writer.writerow(["result", "error"])
                # perform operation and process each line
                for row in read:
                    *nums, op = row
                    nums = [float(x) for x in nums]
                    #match opperators to the calculation
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
                    #write result and error code to output file
                    writer.writerow([result if result is not None else "", error])
                    #save to history
                    self.save_to_history(filename, ",".join(row), result, error)
# add one processed row to the history list
    def save_to_history(self, filename, operation, result, error_code):
        self.history.append([filename, operation, result if result is not None else "", error_code])

    def history_export(self, export_filename):
        #write full history to csv file
        with open(export_filename, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["input_file", "operation", "result", "error"])
            writer.writerows(self.history)