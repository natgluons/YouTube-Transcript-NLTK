from kedro.pipeline import Pipeline, node
from youtube_nlp.nodes import request_authorization, request_access_token, API_requestvideoIDs_bywatchhistory, YouTube_NLTK_WatchHistory_fromIDs

def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                request_authorization,
                inputs=None,
                outputs="authorization_output",
                name="request_authorization_node",
            ),
            node(
                request_access_token,
                inputs="authorization_output",
                outputs="access_token_output",
                name="request_access_token_node",
            ),
            node(
                API_requestvideoIDs_bywatchhistory,
                inputs="access_token_output",
                outputs="video_ids_output",
                name="API_requestvideoIDs_bywatchhistory_node",
            ),
            node(
                YouTube_NLTK_WatchHistory_fromIDs,
                inputs="video_ids_output", 
                outputs=None,  
                name="YouTube_NLTK_WatchHistory_fromIDs_node",  
            ),
        ]
    )
