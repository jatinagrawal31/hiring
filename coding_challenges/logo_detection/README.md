# Problem Statement
Informed would like to have the ability to be able to detect logos from different documents
and know the organization the log0s belong to. Example for Bank statement documents.

As part of this challenge we would like you to develop a learning algorith that can take an input logo
and determine the company it belongs to. These logos can be of different scale, size and qualities to keep that in consideration while thinking about your approach.

There are 2 pieces to this problem.
1. Determining which organization the logo belongs to - This is the primary problem we would like to see your efforts focused towards.
2. Detecting the actual location of the log itself - This will nice to have if you have the time for it.


# Inputs
We have provided some some sample images in the directory `training_images`. These are a mix of differnt types of images.
Some are just the logos, some have text around them.
Fell free to use your own training data as well as you find suitiable, with publicily available images from the internet
having appropriate usage rights.

# Expected output.

There are 2 ouput we expect for this problem
1. A document listing out your approach and different algorithms considered.
   Let us know why you picked an approach and what kind of tweaking needed to be done. If you prefered one algorith over
   another it would be very helpful if you could provide your reasoning

2. We should be able to run a script to determine which organization an input logo file/document belongs to.
   ###Example
   ```
   python logo_detection.py bank_of_america.jpg
   # OR
   python logo_detection.py bank_of_america_statement_page_1.jpg
   ```

   ### Sample Output
   ```
   Document belongs to organization: "Bank Of America"

We are expecting outputs to **only** belong to the following categories:
   ```
   ['Bank Of America', 'Wells Fargo', 'JPMorgan Chase', 'Citigroup Inc', 'Capital One', 'Other']
   ```
