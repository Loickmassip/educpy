from datetime import datetime


def record_result(result):
    file = open("result.txt", "w")
    today=datetime.now()
    strdate=today.strftime("%d-%b-%Y (%H:%M:%S.%f)") + " " + result
    file.write(strdate)


if __name__ == "__main__":
  print("Welcome to EducPy Calculator, please enter your values")
  # Input values
  # call record_result once calculation is done  


