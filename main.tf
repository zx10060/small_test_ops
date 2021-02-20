provider "google" {

  credentials = file("credentinals.json")

  project = "inlaid-contact-305416"
  # region  = "us-central1"
  # zone    = "us-central1-c"
}
