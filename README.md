# Craigslist-WebScraping-Full-Stack-App

Creating more Interactive and beautiful craigslist using Django,python,materialize,HTML,CSS,BeautifulSoup,Database,WebScrapping

The following craigslist app is built on top of https://bangalore.craigslist.org/
Steps followed to build this interactive craigslist:
1.created base.html file under templates using Materialize-css for much interactive UI
2.created models consisting of Search (textfield)
3.Created new_search.html under templates/Mr_NO_ONEApp which iniherits base.html and adds functionality of seraching results based on serach keyword 
4.created Views :
          a.'/' url pointing to base.html
          b.'new_search' pointing to new_search.html
5.created filters under views using BeatuifulSoup to parse html and differentiate product_price,product_url,Ptoduct_name_product_image
6.Appeneded filters to new_search.html to display in an intyeractive way .

Ping me @ gmail: likithKrish31@gmail.com



