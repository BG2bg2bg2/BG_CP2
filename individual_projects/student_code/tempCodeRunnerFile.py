  def class_summary(self):
        count = len(self.students)
        if count == 0:
            print("There are no students in the list")
            return
        total = 0.0
        for i in self.students:
            total += i.get_average_score()

