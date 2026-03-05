from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_in_pinecone
from typing import List

pdf_path = "./resources/HRPolicy.pdf"
def run():
    # Read HR Policy PDF and extract text
    pages = read_pdf(pdf_path)
    # print(f"Extracted {len(pages)} pages from the PDF.")
    # print("First page content:")
    # print(pages[0] if pages else "No content found.")

    # # Chunk the extracted text into manageable pieces
    chunks = chunk_pages(pages, chunk_size=900, chunk_overlap=150)
    print(f"Total chunks created: {len(chunks)}")
    print("First chunks:")
    print(chunks[0])


    embedded_chunks = embed_chunks(chunks)
    print(f"Total chunks embedded: {len(embedded_chunks)}")
    print(f"First chunk embedding: {embedded_chunks[0]}")
    
    store_in_pinecone(chunks, embedded_chunks, namespace="")
   
    
if __name__ == "__main__":
    run()