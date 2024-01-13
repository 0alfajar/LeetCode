import pandas as pd

def getDataframeSize(players: pd.DataFrame) -> List[int]:
    array = [players.shape[0], players.shape[1]]
    return array