import arxiv
import os
import re
from typing import Optional
import requests

class Arxiv:
    
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    download_path = "./downloads/papers/"
    full_path = os.path.join(BASE_DIR, download_path)

    def __init__(self):
        if not os.path.exists(Arxiv.full_path):
            os.makedirs(Arxiv.full_path)

# Arxiv module not working idk why
    '''
    # Search for papers - Top 10 results
    def search(self, query: str):
        search = arxiv.Search(
            query=f'id:{self.id}',
            max_results=1,
            sort_by=arxiv.SortCriterion.SubmittedDate
        )
        result = list(search.results())
        if len(result) == 0:
            raise ValueError(f"No paper found for paper '{self.id}'")
        result = result[0]
        

        result.pdf_url = re.sub(r'v\d+$', '', result.pdf_url)
        title = result.title
        summary = result.summary
        print(result,title)


    # Download Paper
    def download(self, paper):
        paper.download_pdf(dirpath=Arxiv.download_path)
    '''

    @classmethod
    def download(self, id: str):
        url = f"https://arxiv.org/pdf/{id}.pdf"
        data = requests.get(url, allow_redirects=True)
        with open(f"{Arxiv.full_path}{id}.pdf", 'wb') as f:
            f.write(data.content)

        print('File Downloaded Successfully.')
