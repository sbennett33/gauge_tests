# Video Upload Secification

Test a round trip of uploading a video and playing it back

## Upload and playback a video

TODO: Get an upload URL for the video resource
TODO: Use the upload URL to upload a video
TODO: Wait for a webhook notification. Timeout after "20" seconds.
TODO: Verify the playback URL in the webhook notification.

* Get an access token with "namespaces:gauge-test:videos:*" scope
* Create a video resource in the "gauge-test" namespace

---
* Delete video resource from the "gauge-test" namespace
