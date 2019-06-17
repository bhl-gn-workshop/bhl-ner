import random
import time
import sys
import os
import grpc
import protob_pb2
import protob_pb2_grpc as bhl_grpc
import math

#integration with GRPC
class gRPCClient():
    def __init__(self):
        channel = grpc.insecure_channel('bhlrpc.globalnames.org:80')
        self.stub = bhl_grpc.BHLIndexStub(channel)

    def version(self):
        return self.stub.Ver(protob_pb2.Void())
    
    def titles(self):
        return self.stub.Titles(protob_pb2.TitlesOpt())
    
    def pages(self):
        return self.stub.Pages(protob_pb2.PagesOpt(title_ids = [1, 2], with_text = True))

def main():
    client = gRPCClient()
    version = client.version().value
    print(version)
    for page in client.pages():
        #print(page.text)
        for name in page.names:
            print(name.value)
    #res = client.query_stream(queryPages(page_count, number_of_pages))
    

    
if __name__ == '__main__':
    main()