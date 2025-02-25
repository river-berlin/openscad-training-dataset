# openscad-training-dataset
A refined training dataset for openscad projects - with a focus on BOSL2


## Current list of ideas with checkmarks

1. [] - Manual labelling, and creating the dataset (in progress)
2. [] - Fine tuning a model on (1) as I am working on it, so that my future progress becomes faster
3. [] - Expanding orientations and using a large language model to create combinations of how to do things on the existing dataset
4. [] - Filtering out BOSL2 from existing datasets on huggingface and using those datasets perhaps?

## Modelling prompt

I didn't exactly use this for everything, but something close to this :)

```
I am creating a dataset to "fine tune" a model to produce chain-of-thought responses, Given the following prompt and response, could you convert the response to a chain-of-thought answer please?

The response must consider

1. The assumptions being made - i.e. wordings changed possibly, and why those assumptions are being made
2. The position, size and orientation of the object relative to the object asking to be modified/changed (so if someone says, put a box on the right of the sphere, one needs to take into account the position and size of the sphere)
3. The new size and orientation of the object added/changed
4. Then on the basis of the above 2 points, come up with an answer to where the object should be placed
5. If an image is added to the response - be extra descriptive of the image (to reduce ambiguity in the final result)

do not add any extra details to the response (such as "here is the new response"), to the start or end - to make it easy to paste the new response in a spreadsheet

Prompt
----------
make me a semicircle in openscad

Response
-------------
here is the response

linear_extrude(height=5) {
    intersection() {
            circle(50);
            translate([-50, 0, 0]) square([100, 50], center=false);
    }
```