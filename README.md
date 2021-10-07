# Steroids or Not

> (hopefully) A computer vision classifier that detects whether fit people have used steroids or not, using an image as input.

Built using:

- Fast.AI to train the model
- nbdev to support the workflow
- Jupyter Notebooks for experimentation as well as final code
- Paperspace Gradient for training hardware
- PRAW to extract data from Reddit
- Pushshift as a third party workaround for Reddit's limited API
- SQLite as a database to keep data organized

## Install

Clone this repo, then run 

`pip install .[dev]`

`cp .sample-env .env` then fill in environment variables (so far just reddit api stuff).

### Useful jupyter extensions

```
jupyter nbextension install https://github.com/drillan/jupyter-black/archive/master.zip --user
jupyter nbextension enable jupyter-black-master/jupyter-black
nbdime extensions --enable --user
jupyter nbextension enable --py widgetsnbextension
```

## Testing

Many tests, including those tagged `local` or `all_local` don't run on github actions because it doesn't have the data available and I haven't prioritized figuring out some fixtures. To run all the tests, run `nbdev_test_nbs --flags local`. That's what the `all_local` comments mean, they are nbdev comments.

## Database

I think this should create the database? 
```
import steroidsornot.database
```
And now migrate the database.
```
alembic upgrade head
```