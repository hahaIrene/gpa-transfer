import pandas as pd

def gpaCalculate(scores):
    getData = pd.read_csv(scores)
    toGpa = {
    "A+": 4.0,
    "A": 4.0,
    "A-": 3.67,
    "B+": 3.33,
    "B": 3.0,
    "B-": 2.67,
    "C+": 2.33,
    "C": 2.0,
    "C-": 1.67,
    }


    getData["GPA"] = getData["成績"].map(toGpa)

    filtered_df = getData[getData["備註"].fillna("").str.contains("另計") == False]
    total_credit = filtered_df["學分"].sum()
    weighted_gpa = (filtered_df["GPA"] * filtered_df["學分"]).sum() / total_credit
    

    return weighted_gpa



if __name__ == "__main__":

    my_scores = r'./scores.csv'
    result = gpaCalculate(my_scores)

    print(result)