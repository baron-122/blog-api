# blog-api
# blog-api


Create a post
POST METHOD
URL : https://blog-api-h3qs.onrender.com/posts


Fetch all posts from DB
GET METHOD
URL : https://blog-api-h3qs.onrender.com/posts


Fetching a single post - by id  from DB
GET METHOD
URL : https://blog-api-h3qs.onrender.com/posts/1

Updating post by id
UPDATE METHOD
URL : https://blog-api-h3qs.onrender.com/posts/1

Deleting post by id
DELETE METHOD
DELETE https://blog-api.onrender.com/posts/1



Below is a input and expected response from the
GET METHOD
URL : https://blog-api-h3qs.onrender.com/posts

sample request payload

{
  "title": "Vampires, Real or Folktales",
  "content": "Children of night, blood suckers, night walkers these creatures have many names but,...."
}

sample response payload

[
    {
        "content": "We have heard many stories about big foot prints in the snow",
        "created_at": "2025-08-26 20:43:50",
        "id": 1,
        "title": "Big foot, Myth and Facts"
    },
    {
        "content": "Children of night, blood suckers, night walkers these creatures have many names but,....",
        "created_at": "2025-08-26 20:46:46",
        "id": 2,
        "title": "Vampires, Real or Folktales"
    }
]
