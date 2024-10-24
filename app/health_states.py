from app import base


class Health_states():

    fileName = '../user_data_files/health_states.json'

    def __init__(self):
        """
        initializer / constructor
        """
        self.date = None
        self.health_states = []
        self.fileName = '../user_data_files/health_states.json'
        self.weight: float = 0
        self.height: float = 0
        self.measure_date = ""
        self.bmi: float = 0

    def add_health_states(self, weight: float, height: float, date: str):
        """
        method adds health states to file
        :param weight:
        :param height:
        :param date:
        :return:
        """
        self.weight = weight
        self.height = height
        self.bmi = self.calc_bmi(weight, height)
        self.date = date

        new_measurement = {
            "height": height,
            "weight": weight,
            "bmi": self.calc_bmi(weight, height),
            "date": self.date

        }
        self.health_states.append(new_measurement)
        base.save_to_file(self.fileName, self.health_states)
        print(">> Health States saved successfully ✅ ")

    def calc_bmi(self, weight: float, height: float) -> float:
        """
        method calculates and return the current bmi of the user
        :param weight:
        :param height:
        :return: bmi
        """
        height = height / 100
        bmi: float = round(weight / (height ** 2), 2)
        return bmi

    def get_health_states(self):
        """
        this method displays all records of the health states from files
        :return:
        """
        self.health_states = base.load_from_file(self.fileName)
        self.formatOutput()

    def bmi_categorization(self, bmi):
        """
        this method categorize user bmi and returns the appropriate msg
        :param bmi:
        :return:
        """
        if bmi < 18.5:
            # print("You are classified as Underweight, which may increase the RISK of developing health problems")
            return "Underweight"
        elif 18.5 < bmi < 24.9:
            # print("Nice, you are at the normal range of weight, we hope you keep it that way to avoid health problems")
            return "Normal"
        elif 25.0 < bmi < 29.9:
            # print("You are classified as OVERWEIGHT, which may INCREASE the RISK of developing health problems")
            # print("watch your weight, and maintain a healthier life style and workout")
            return "Overweight"
        elif 30 < bmi < 34.9:
            # print("You are classified as OBESE CLASS I, which may have HIGH RISK of developing health problems")
            # print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")
            return "Obese Class I"
        elif 35 < bmi < 39.9:
            # print("You are classified as OBESE CLASS II, which may have VERY HIGH RISK of developing health problems")
            # print("Be careful, your at risk please consider visiting the Nutritionist and take regular health checks")
            return "Obese Class II"
        elif bmi > 40:
            # print("You are classified as OBESE CLASS III, which may have EXTREMELY HIGH RISK of developing health problems")
            # print("Be careful, you're at risk please consider visiting the Nutritionist and take regular health checks")
            return "Obese Class III"

    def track_progress(self):
        """
        this method should be able to analyse all records of the health states and returns progress data
        :return:
        """
        pass
        # todo track progress

    def formatOutput(self):
        """
        Formats and prints a task from the to-do list.
        """
        if (len(self.health_states)) > 0:
            print("-"*30)
            for i, state in enumerate(self.health_states, start=1):
                print(f"{i}. Height: {state['height']} CM, Weight: {state['weight']} KG And BMI: {state['bmi']}, "
                      f" Measurement Date: {state['date']}")
            print("-"*30)
        else:
            print("No Data Available")

    def remove_state(self, num):
        self.health_states = base.load_from_file(self.fileName)
        if len(self.health_states) > 0:
            del self.health_states[num - 1]
            base.save_to_file(self.fileName, self.health_states)
            print("State is Deleted Successfully")
        else:
            print("States are not available")
