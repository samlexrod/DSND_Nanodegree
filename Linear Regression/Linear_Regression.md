```
$$
\frac{n!}{k!(n-k)!} = {n \choose k}
$$
```

# Tricks

Variables:

$\alpha=$ *Learning Rate*

$p=$ *Horiontal Coordinate x*

$q=$ *Vertical Coordinate y*

## Absolute Trick

$$y=mx+b$$

$y=(m+p\alpha)x+b\alpha$

## Square Trick

Key Differences:
> - We add the distance between Vertical Coordinates.
> - We solve for $y$ to find $q^{\prime}$.

$q-q^{\prime}=$ *Distance between Vertical Coordinates*

$y=(m + p\alpha(q-q^{\prime}))x+ba(q-q^{\prime})$


# Regression


## Mean Absolute Deviations (Error)

$m=$ *Number of Points in the Dataset* 

$y=$ *Actual Value*

$\hat{y}=$ *Predicted Value*

$\sum_{i=1}^m|y-\hat{y}|=$ *Deviations (Error)*

$\frac{\sum_{i=1}^m|y-\hat{y}|}{m}=$ *Mean Absolute Deviations (Errors)*


## Mean Squared Deviations (Error)

$\frac{\sum_{i=1}^{m}(y-\hat{y})^2}{2m}=$ *Mean Squared Deviations (Errors)*

