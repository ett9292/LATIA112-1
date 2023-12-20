def azure_sentiment(user_input):
    text_analytics_client = TextAnalyticsClient(
        endpoint=config['AzureLanguage']['END_POINT'], 
        credential=credential,
        language="zh-Hant",
        include_score=True)
    
    documents = [user_input]
    response = text_analytics_client.analyze_sentiment(
        documents, 
        show_opinion_mining=True)
    
    docs = [doc for doc in response if not doc.is_error]
    for idx, doc in enumerate(docs):
        print(f"Document text : {documents[idx]}")
        print(f"Overall sentiment : {doc.sentiment}")
        print(f"Sentiment score : {doc.confidence_scores[doc.sentiment]}")
        
        # 獲取主詞
        if doc.sentences and doc.sentences[0].mined_opinions:
            opinions = doc.sentences[0].mined_opinions
            aspect_str = ', '.join(opinion.aspect for opinion in opinions)
            print(f"Aspects : {aspect_str}")
    
    return f"情感: {doc.sentiment}, 分数: {doc.confidence_scores[doc.sentiment]}, 主詞: {aspect_str}"

