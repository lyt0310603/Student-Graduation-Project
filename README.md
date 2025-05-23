# Work Flow
1. Web Crawler
2. Label
3. Build Model
4. Google Extension
5. Backend

## Web Crawler
### Use selenium and beautifulsoup in Python, craw on [Bahamut NCU](https://forum.gamer.com.tw/C.php?page=1&bsn=60076&snA=4671705).

### We get content, reply, post time and floor from each article, and make a NCU_dataset.csv which contain 20891 articles.
![](https://github.com/lyt0310603/Student-Graduation-Project/blob/main/README_Pic/bahamut.png)
## Label
### Use [Lable Studio](https://labelstud.io/) for  labeling task.
### we have many label as the pictue show. ![](https://github.com/lyt0310603/Student-Graduation-Project/blob/main/README_Pic/label_studio.png)To avoid too many label to make model learning diffcult, generalize similar label in one. Finally we extract the 5 most frequency label as below, and a 6th label is 其他(else).
* 課業
* 生活
* 食物
* 問題
* 蓋樓
### Due to time and human resources limit, we finally completed 9500 labeling task in 20891.

## Build Model

### We try many different model for this multilabel-classify task, like ML-KNN, fullconnective network(use tensorflow), and pretrained model on transformers(bert-base-chinese, bert-base-multilingual and so on). Finally, after compare accuracy and other metrics, we decide to use Bert-base-chinese for our task.

### Comparing Table: P is precision, R is recall, f1 is F1-score
![](https://github.com/lyt0310603/Student-Graduation-Project/blob/main/README_Pic/compare_table.png)
## Google Extension
### Download Link: [Here](https://chrome.google.com/webstore/detail/%E5%B7%B4%E5%93%88%E5%A7%86%E7%89%B9-%E4%B8%AD%E5%A4%AE%E4%B8%B2%E5%88%86%E6%9E%90/cffglllonpmkobnlbcbechbnmocaadhl)
### Use background.js to check the page updete, and if the page is Bahamut NCU then send a reuest ro content.js to get article contents. After get contents, send it to backend.
### After open extension ![](https://github.com/lyt0310603/Student-Graduation-Project/blob/main/README_Pic/extension_result.jpg)
## Backend
### Use Flask to build a beckend, and return predict output to extension.
### Put the flask website on [DigitalOcean](https://www.digitalocean.com/) droplet(VM).
