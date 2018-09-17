Box Detection
=============

Guidelines
----------
* Organize, test, and document like you would on Production
* Send us a link to the hosted repository (GitHub, Bitbucket, ...)

Task
----
Create a service that will detect all the boxes in a given document.

It should take the following parameters:
* `input_file`: Local file path of the input document in which to detect the boxes
* `output_file`: Local file path of the output document in which to draw the detected boxes

Apart from drawing the boxes in the `output_file`, the service should also return the co-ordinates of the detected boxes in JSON format.

Example Response:
```
{
    "boxes": [
        {
            "points": [
                [
                    90,
                    838
                ],
                [
                    75,
                    838
                ],
                [
                    75,
                    851
                ],
                [
                    90,
                    851
                ],
                [
                    90,
                    838
                ]
            ]
        },
        {
            "points": [
                [
                    327,
                    840
                ],
                [
                    313,
                    840
                ],
                [
                    313,
                    853
                ],
                [
                    327,
                    853
                ],
                [
                    327,
                    840
                ]
            ]
        },
        .
        .
    ]
}
```


Examples
--------
For your convenience, we have uploaded a few test documents in the `examples/inputs` directory. You can choose to test on those documents or any documents of your choosing. We encourage you to test across different documents time permitting for better outcomes.

We have also uploaded a few examples of what we expect the output files to look like in the `examples/outputs` directory. (The ID values inside each box is not required)

Running
-------
Make sure we can run your code using our provided helper script
Example: `python detect_boxes.py './examples/inputs' './examples/outputs'`

Here `examples/outputs` directory, will contain the output images with boxes highlighted, as well
as a separate `JSON` file for each input image with co-ordinates of detected boxes.
