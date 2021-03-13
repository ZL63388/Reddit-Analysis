import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

def load_css(file_name:str)->None:
    """
    Function to load and render a local stylesheet
    """
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css("style.css")

my_page = st.sidebar.radio('Contents', ['Introduction', 'Data Information', 'Methodology', 'NLP Workflow','EDA' ,'Classification Model','Post EDA','Regression Model','Pipeline','Conclusion & Recommendation'])
if my_page == 'Introduction':
    col1, mid, col2 = st.beta_columns([1,3,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("A Subreddit Analysis on Jokes")
    st.image('status.PNG', use_column_width='auto')
    st.header("Introduction")
    st.markdown("The purpose of this project is to provide an analysis on subreddits related to \
        jokes by implementing **Natural Language Processing Techniques** and by applying a **Classification \
        and Regression Model** to identify which jokes will have high engagements.")
    st.write("\n\n")
    st.header("What is Reddit?")
    st.markdown("**Reddit** is a network of communities based on people's interests. \
        Forums on the Reddit platform are called **subreddits**. Users can use a subreddit \
        to create new posts on a specific topic. These can be questions and requests for help, \
        but also informative news articles, images, and videos.")
    st.write("\n\n")
    st.header("But why did we choose Jokes?")
    st.markdown('Do you believe that something so simple as a joke can actually be used as a power \
        move by companies or brand alike. Brands can reach their audience through **humor**.\
        This claim is backed up by multiple researches. One of which is **The Influence of Humor Strength and Humor-Message \
        Relatedness onAdMemorability: ADual ProcessModel** \n \
        \n "The study shows the impact of humorous advertisements are more on **recall of ads, and ad memorability**, \
        the humor get attention and mood when the humor appeal is strong, the positive influence of mood created by humor and product relatedness made."\
        \n-Cline and Kellaris, 2007')
    st.markdown("Other researchers in the effects of using humor:")
    st.markdown('**Gets people to listen** - "Let the Good Times Roll Building of a Fun Culture" \
        David Stauffer, Harvard Management \
        \n**Increases long term memory retention** - "Relationship between Instructor and Student \
        Learning" M Wanzer, Communication Education \
        \n**Helps communicate messages** - "Does Humor Use Enhance SpeakerEthos?" C Ellis Campbell,\
        Association for Applied and Therapeutic Humor.\
        \n**Builds trust** - "Humor in the Workplace: A Communication Challenge",\
        Robert A. Vartebedian, Speech Communication Association\
        \n**Improves likeability** - "A funny thing happened on the way to the bottom line",\
        B.J. Avollo, Academy of Management Journal')
    st.markdown("To name a few brands in the Philippines using humor as advertising strategy, \
        **Angkas** posted on **Facebook** last March 4, 2021. This post garnered a total engagements of \
        **32k likes, 1.7k comments, and 8.7k shares**.")
    st.image('fb.PNG',use_column_width='auto',caption="Angkas Facebook Post")
    st.write("\n")
    st.markdown("**RC Cola Philippines** tweeted its advertising video on **Twitter** last \
        November 26, 2020. This tweet garnered a total engagements of \
        **20.6k likes, 1.5 retweets, and 8.6 quote retweets**.\
        In fact, this commercial was also featured in an international\
        tv show, **The Ellen Show**.")
    st.write("\n\n")
    st.video('https://www.youtube.com/watch?v=9zrExsQpQhU&t=3s')
    st.write("\n\n")
    st.markdown("With research and real examples, the usage of Jokes in campaigns is\
        relevant because of the strong positive influence it gives to the audience.")
    st.write("\n\n")
    st.header("The team's objectives:")
    st.markdown("1.    Analyze the joke subreddits by using Natural Language Processing Techniques")
    st.markdown("2.    Identify which jokes will have high engagements through a Classification and Regression model")  


elif my_page == 'Data Information':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Data Information")
    st.image('status.PNG', use_column_width='auto')
    st.write("\n\n")
    st.image('reddit_post.PNG', use_column_width='auto')
    st.subheader("**Title**: The title of the submission.")
    st.subheader("**Self text**: The submissions’ selftext - an empty string if a link post.")
    st.subheader("**Upvote**: The number of upvotes for the submission.")
    st.subheader("**Downvote**: The number of downvotes for the submission.")
    st.subheader("**Upvote ratio**: The percentage of upvotes from  all votes on the submission.")
    st.subheader("**Number of comments**: The number of comments on the submission.")
    st.subheader("**NSFW**: Whether or not the submission has been marked as NSFW.")
    st.subheader("**Label**: Joke subreddit classification.")

elif my_page == 'Methodology':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Methodology")
    st.image('status.PNG', use_column_width='auto')
    st.write("\n\n")
    st.image('methodology.png',use_column_width='auto')

elif my_page == 'NLP Workflow':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("NLP Workflow")
    st.image('status.PNG', use_column_width='auto')
    st.write("\n\n")
    st.image('nlp.png', use_column_width='auto')
    st.write("\n\n")

elif my_page == 'EDA':
    col1, mid, col2 = st.beta_columns([1,3,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Exploratory Data Analysis")
    st.image('status.PNG', use_column_width='auto')
    st.write("\n")
    st.subheader("**Wife_jokes** has the **highest number of comments** while antijokes has the least number of comments.")
    st.write("\n\n")
    st.image('eda1.PNG',caption="Number of Comments among Subreddits", use_column_width='auto')
    st.write("\n\n")
    st.subheader("**Wife_jokes** has the **highest number of upvotes** while antijokes has the least number of upvotes.")
    st.write("\n\n")
    st.image('eda2.PNG',caption="Number of Upvotes among Subreddits", use_column_width='auto')
    st.write("\n\n")
    st.subheader("**Correlation of Upvotes and Comments**")
    st.write("\n\n")
    st.subheader("Although the number of comments and upvotes are highly correlated, we still recommend analyzing them separately.")
    st.write("\n\n")
    st.image('eda3.PNG',caption="Number of Upvotes among Subreddits", use_column_width='auto')
    st.write("\n\n")

elif my_page == 'Classification Model':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Classification Model")
    st.image('status.PNG', use_column_width='auto')
    st.header("**Random Forest Classifier**")
    st.write('\n\n')   
    st.subheader("Trained on 11,401 and tested on 1,267 jokes")
    st.subheader("")
    st.image('confusion_matrix.png', caption="Confusion Matrix", use_column_width='auto')
    st.header("Accuracy scores:")
    st.subheader("5-Fold CV Training: 69%")
    st.subheader("Test score: 71%")

elif my_page == 'Post EDA':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Post EDA")
    st.image('status.PNG', use_column_width='auto')
    st.header("**Joke Classification**")
    st.image('posteda1.PNG', use_column_width='auto')
    st.header("**Joke Category Descriptions**")
    st.subheader("The **Wife joke category** is focused on jokes related to male stereotypes, and punchlines related to man doing activties.")
    st.subheader("The **Dark joke category** is focused on jokes which involve controversial topics related to politics, sexism, racism, and culture.")
    st.subheader("The **3am joke category** is focused on jokes related to sleep deprivation and punlike structured jokes.")
    st.subheader("The **Anti joke category** is focused on jokes which are structured as non-jokes but received by the audience as funny.")
    st.subheader("The **Dad joke category** is focused on jokes which revolved are structured by using family relations such as husband-wife or parent-child relationships.")

elif my_page == 'Regression Model':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Regression Model")
    st.image('status.PNG', use_column_width='auto')
    st.header("**Regression Model - Random Forest**")
    st.write("\n")
    st.header("**Features used:**")
    st.subheader("joke class")
    st.subheader('"NSFW" tag')
    st.subheader("TF-IDF array")
    st.write("\n")
    st.header("**Target variable:**")
    st.subheader("Number of upvotes")
    st.subheader("May also use the **Number of Comments** as another target")
    st.write("\n")
    st.header("**Trained on 11,401 and tested on 1,267 jokes**")
    st.write("\n")
    st.header("**R² scores:**")
    st.subheader("5-Fold CV Training: **59%**")
    st.subheader("Test score:  **61%**")

elif my_page == 'Pipeline':
    col1, mid, col2 = st.beta_columns([1,8,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Pipeline")
    st.image('status.PNG', use_column_width='auto')
    st.image('pipeline.PNG', use_column_width='auto')

elif my_page == 'Conclusion & Recommendation':
    col1, mid, col2 = st.beta_columns([1,2,20])
    with col1:
        st.image('reddit_logo.png', width=100)
    with col2:
        st.title("Conclusion & Recommendation")
    st.image('status.PNG', use_column_width='auto')
    st.write("\n\n")
    st.header("**Conclusions**:")
    col1, mid, col2 = st.beta_columns([1,3,20])
    with col1:
        st.write("\n")
        st.image('c1.PNG', width=100)
        st.write("\n")
        st.image('c2.PNG', width=100)
        st.image('c3.PNG', width=100)
    with col2:
        st.header("**wife_jokes** have the **highest** number of engagements while the antijokes have the least.")
        st.header("Subreddit classification heavily depends on **key words** present")
        st.header("Both **upvotes** and **comment count** can be used simultaneously as measures of engagement.")
    st.header("**Recommendation**:")
    col1, mid, col2 = st.beta_columns([1,3,20])
    with col1:
        st.write("\n")
        st.image('r1.PNG', width=100)
        st.write("\n")
        st.image('r2.PNG', width=100)
        st.image('r3.PNG', width=100)
        st.image('r4.PNG', width=100)
    with col2:
        st.header("**Add more data** to potentially improve joke classification")
        st.header("")
        st.header("**Add more features** to potentially improve the performance of the models")
        st.header("")
        st.header("**Clean** the data further")
        st.header("")
        st.header("**Perform image analysis** for 'image-type' jokes (e.g. memes)")
    st.write("\n")