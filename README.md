### Steps to make the project:
  1. download 'compVsnifty.pkl' file from compVsnifty and 'nasdaqVsnifty.pkl'nasdaqVsnifty directory.
  2. download 'Bert_Sentiment_analysis.ipynb' file from sentiment analysis directory and run it to download the model saved in 'sentiment_analysis.pth' file.
  3. download 'merging_models.ipynb' file from final merge of models directory.
  4. for compVsnifty model take these as user input(make sure you give them to the model in the same order):
         'Infosys net profit',
         'Nifty change_profit',
         'Nifty change_close',
         'TCS change_profit',
         'Infosys change_profit',
         'HCL change_profit',
         'Nifty change_sales',
         'TCS change_sales',
         'Infosys change_sales',
         'Last_close'.
  5. for nasdaqVsnifty model take these as user input(make sure you give them to the model in the same order):
         'nasdaq_close_percentage_change',
         'nifty_close_percentage_change',
         'nasdaq_open_percentage_change',
         'nifty_open_percentage_change',
         'nasdaq_high_percentage_change',
         'nifty_high_percentage_change',
         'nasdaq_low_percentage_change',
         'nifty_low_percentage_change'.
  6. Scrap data from website using the '.ipynb' given, convert scraped data to list and give to 'sentiment_analysis.pth'
  7. Use blockchain smartcontract to change the weights list in 'merging_models.ipynb' until the 'final_pred' comes accurate with high chances. you can increase weight by 0.05
in each iteration.
