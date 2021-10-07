# Steroids or Not

> (hopefully) A computer vision classifier that detects whether fit people have used steroids or not, using an image as input.

## Technology

Built using:

- Fast.AI to train the model
- nbdev to support the workflow
- Jupyter Notebooks for experimentation as well as final code
- Paperspace Gradient for training hardware
- PRAW to extract data from Reddit
- Pushshift as a third party workaround for Reddit's limited API
- SQLite as a database to keep data organized
- Alembic to simplify database interactions
- [r/nattyorjuice](https://www.reddit.com/r/nattyorjuice/) as a data source


## Data caveats
It is not completely based in ground truth, as r/nattyorjuice is educated guesses, not admitted steroid use, which complicates prediction. However, the comments often describe objective, observable criteria which is often based in the user's own steroid use.

## Results

After about a month and half of working on it full time, the last attempt that I made to train the classifier was right on the line of predicting the labels better than chance. The classifier was overfitting, I think it just needed more data but I wasn't certain how to tell why it was not predicting labels better than chance. The task set before the machine learning model may have also been complicated by the subjects being in different poses, with varying amounts of clothing, messy backgrounds, multiple people in the photo, etc. In any case, this project required months more work to make it work properly, and I had other things I wanted to do, so I moved on.
    

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