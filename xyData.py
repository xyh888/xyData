from util import load_json_settings

class CTPFuture():
    def __init__(self,db="vnpy"):
        config = load_json_settings("mongodb_settings.json")
        print(config)






if __name__ == "__main__":
    ctpData = CTPFuture()