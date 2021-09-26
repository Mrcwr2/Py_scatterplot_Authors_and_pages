import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

with open("books.csv","r") as datafile:
    data = pd.read_csv(datafile,delimiter=",")

sns.scatterplot(x="# num_pages", y="ratings_count", size="ratings_count", sizes=(20, 180), data=data)

plt.xlabel("# num_pages")
plt.ylabel("Rating")
plt.title("Average Rating & Pages")
plt.savefig("Author_Rating.png")