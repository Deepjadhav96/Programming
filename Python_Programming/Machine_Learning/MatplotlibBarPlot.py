import matplotlib.pyplot as plt



def main():
    language = ["C","CPP","Java","Python"]
    student = [30, 40, 35, 55]

    plt.bar(
        language,                      #Value of X axis
        student,                       #Value of Y axis
        width=0.6,                      #width of bars
        edgecolor = "black",            #Border color of bar
        linewidth = 1,                  #width of bar border
        alpha = 0.8,                    #transpenrence 0.0 to 1.0
        label = "Students"              #legend text
    )

    plt.title("Marvellous Bar Graph")

    plt.xlabel("Languages")
    plt.ylabel("Number of student")

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()