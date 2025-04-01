from src.auth import get_imgur_auth


def main() -> None:
    # get authenticated imgur object
    im = get_imgur_auth()

    user = im.get_user("me")

    # for whatever reason, if this is called without a limit, it will return 100
    # hardcoding limit of 1000 to get all images, but if images are more than 1000, it will return 1000 images
    # this 100 limit is enforced by the imgur api, so we need to use the limit parameter to get all images
    images = user.get_images(limit=1000)
    print(f"Found {len(images)} images")

    ## get folder name
    ## scan every md file for imgur links

    ## compare detected imgur links from md files with with imgur api links
    ## output imgur api links that are not in md files


if __name__ == "__main__":
    main()
