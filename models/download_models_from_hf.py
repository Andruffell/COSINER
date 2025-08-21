from transformers import AutoModel, AutoTokenizer

bert = AutoModel.from_pretrained("bert-base-uncased")
bert.save_pretrained("./models/BERT/", from_pt = True)

bert_tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
bert_tokenizer.save_pretrained("./models/BERT/TOKENIZER")

biobert = AutoModel.from_pretrained("dmis-lab/biobert-v1.1")
bert.save_pretrained("./models/BioBERT/", from_pt = True)

bert_tokenizer = AutoTokenizer.from_pretrained("dmis-lab/biobert-v1.1")
bert_tokenizer.save_pretrained("./models/BioBERT/TOKENIZER")