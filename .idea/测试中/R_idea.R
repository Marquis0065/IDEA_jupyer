library(rvest)
#https://sz.lianjia.com/zufang/nanshanqu/pg2rt200600000001l1/#contentList
base_url = 'https://sz.lianjia.com/zufang/'
district = 'luohu'
price <- c()
for(i in 1:11){
  url = paste(base_url,district,'qu/pg',i,'rt200600000001l1/#contentList',sep = '')
  result <- read_html(url) %>% html_nodes(xpath='//em') %>% html_text()
  result <- result[-length(result)]
  price <- c(price,result)
}
length(price)
data = as.numeric(price)[as.numeric(price)<10000]
hist(data,main = district)

library(reticulate)
repl_python()

import os





