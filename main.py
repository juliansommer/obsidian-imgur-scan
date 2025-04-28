from src.auth import get_imgur_auth
from src.folder import open_folder
from src.matches import find_matches_in_files


def main() -> None:
    # get authenticated Imgur object
    im = get_imgur_auth()

    user = im.get_user("me")

    # for whatever reason, if this is called without a limit, it will return 100
    # hardcoding limit of 1000 to get all images, but if images are more than 1000, it will return 1000 images
    # this 100 limit is enforced by the Imgur api, so we need to use the limit parameter to get all images
    images_objects = user.get_images(limit=1000)

    image_links = set()

    # get all image links from the images object
    for image in images_objects:
        image_links.add(image.link)

    path_input = open_folder()
    print(f"Selected folder: {path_input}")

    regex = r"https://i\.imgur\.com/\w+\.\w+"

    # find all links in md files
    found_links = find_matches_in_files(path_input, regex, ".md")

    print(f"Found {len(found_links)} links in files")
    print(f"Found {len(image_links)} links in Imgur api")

    # Output links in files that are not in Imgur api
    missing_links = found_links - image_links
    if missing_links:
        print(f"Found {len(missing_links)} links in files that are not in Imgur api")
        for link in missing_links:
            print(link)

    # Output Imgur api links that are not in files
    missing_links2 = image_links - found_links
    if missing_links2:
        print(f"Found {len(missing_links2)} Imgur links not found in files")
        for link in missing_links2:
            print(link)
    else:
        print("All Imgur links are found in files")


if __name__ == "__main__":
    main()
