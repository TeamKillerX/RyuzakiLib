import aiohttp


class AsyicXSearcher:
    """
    A class to handle asynchronous HTTP requests using aiohttp.

    This class provides static methods to perform GET, POST, and HEAD requests asynchronously.
    """

    def init(self):
        pass

    @staticmethod
    async def search(
        url: str,
        post: bool = False,
        head: bool = False,
        headers: dict = None,
        evaluate=None,
        object: bool = False,
        re_json: bool = False,
        re_content: bool = False,
        *args,
        **kwargs,
    ):
        """
        Perform an asynchronous HTTP request.

        Args:
            url (str): The URL to send the request to.
            post (bool): If True, perform a POST request. Defaults to False (GET request).
            head (bool): If True, perform a HEAD request. Defaults to False.
            headers (dict): Headers to include in the request. Defaults to None.
            evaluate (callable): A function to evaluate the response. Defaults to None.
            object (bool): If True, return the response object. Defaults to False.
            re_json (bool): If True, return the response in JSON format. Defaults to False.
            re_content (bool): If True, return the raw response content. Defaults to False.
            *args: Additional arguments to pass to the request method.
            **kwargs: Additional keyword arguments to pass to the request method.

        Returns:
            The result of the request, formatted according to the specified flags.

        Raises:
            DependencyMissingError: If aiohttp is not installed.
        """
        if aiohttp:
            async with aiohttp.ClientSession(headers=headers) as session:
                method = (
                    session.head if head else (session.post if post else session.get)
                )
                async with method(url, *args, **kwargs) as response:
                    if evaluate:
                        return await evaluate(response)
                    if re_json:
                        return await response.json()
                    if re_content:
                        return await response.read()
                    if head or object:
                        return response
                    return await response.text()
        else:
            raise DependencyMissingError("Install 'aiohttp' to use this.")

async def async_search(
    url: str,
    post: bool = False,
    head: bool = False,
    headers: dict = None,
    evaluate=None,
    object: bool = False,
    re_json: bool = False,
    re_content: bool = False,
    *args,
    **kwargs,
):

    if aiohttp:
        async with aiohttp.ClientSession(headers=headers) as session:
            method = (
                session.head if head else (session.post if post else session.get)
                )
            async with method(url, *args, **kwargs) as response:
                if evaluate:
                    return await evaluate(response)
                if re_json:
                    return await response.json()
                if re_content:
                    return await response.read()
                if head or object:
                    return response
                return await response.text()
    else:
        raise DependencyMissingError("Install 'aiohttp' to use this.")
