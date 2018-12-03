# ScrapyCSVSplit

This is a Scrapy pipeline to automatically split CSV output file when it is too large.

Don't forget to activate it in the settings like this:

```
ITEM_PIPELINES = {
   'myproject.pipelines.MyPipeline': 300,   
}
```

https://stackoverflow.com/questions/21009027/split-scrapys-large-csv-file/40654790#40654790
