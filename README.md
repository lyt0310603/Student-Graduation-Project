# Work Flow
1. Web Crawler
2. Label
3. Build Model
4. Google Extension
5. Backend

## Web Crawler
### Use selenium and beautifulsoup in Python, craw on [Bahamut NCU](https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=4671705)
### We get content, reply, post time and floor from each article
![](https://cdn.discordapp.com/attachments/1122916420192309321/1126770109470478346/image.png)
### and make a NCU_dataset.csv which contain 20891 articles

## Label
### Use [Lable Studio](https://labelstud.io/)
### we have many label as the pictue show
![](https://media.discordapp.net/attachments/1122916420192309321/1126774256945078283/image.png?width=1440&height=422)
### to avoid too many label to make model learning diffcult, generalize similar label in one, and finally we extract the 5 most frequency label.
* 課業
* 生活
* 食物
* 問題
* 蓋樓

## Build Model

### We try many different model for this multilabel-classify task, like ML-KNN, fullconnective network(use tensorflow), and pretrained model on transformers(bert-base-chinese, bert-base-multilingual and so on). Finally, after compare accuracy and other metrics, we decide to use Bert-base-chinese for our task.

### comparing table
#### P is precision, R is recall, f1 is F1-score
![](https://cdn.discordapp.com/attachments/1122916420192309321/1126794830253658152/2023-07-07_164000.png)

## Google Extension
###

## Backend
### Use Flask
