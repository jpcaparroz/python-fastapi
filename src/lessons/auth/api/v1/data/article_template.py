from fastapi import Body

from schemas import article_schema as schemas


CreateArticleBody = Body(
    title='Article', 
    description='The article json representation.',
    examples=[
        schemas.ArticleSchema(
            title='Article Ipsum',
            description='It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.',
            source_url='https://twitter.com/home',
            user='9461346a-9b67-4fb3-a181-3121718aed4a'
        )
    ]
)


UpdateArticleBody = Body(
    title='Article', 
    description='The article json representation.',
    examples=[
        schemas.ArticleSchema(
            title='Article Ipsum',
            description='It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout.',
            source_url='https://twitter.com/home',
            user='9461346a-9b67-4fb3-a181-3121718aed4a'
        )
    ]
)