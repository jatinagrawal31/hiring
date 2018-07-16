Box Detection
=============

Guidelines
----------
* Organize, test, and document like you would on Production
* Send us a link to the hosted repository (Github, Bitbucket, ...)

Task
----
Create a service that will detect all the boxes in a given document.

It should take the following paramters:
* `input_file`: URL or a Local file path of the input document in which to detect the boxes
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

Running
-------
Please also create a `run_service.sh` script that will run a server locally on port `5050`
