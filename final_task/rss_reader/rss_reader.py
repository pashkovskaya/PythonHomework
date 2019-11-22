"""
This module provides one-shot command-line RSS rss_reader
"""
import os
import sys
import argparse
import json
import logging
import caching
import news_date
from pathlib import Path
from inspect import currentframe, getframeinfo
from news import News

current_version = "1.0"
log_file_name = 'rss_reader.log'
data_dir_name = 'data'
cache_file_name = 'cache.json'


def print_json(news, indent):
    """
    This function prints news in JSON format
    :param news: RSS news (class News)
    :param indent: indent size of nested structures (int)
    :return: None
    """
    print(json.dumps(news.to_json(), indent=indent))


def print_message(message, is_error=False):
    """
    This function prints errors to stdout in specified format
    :param message: message to be printed
    :param is_error: defines if message is error message
    :return: None
    """
    if is_error:
        print(f'rss-reader: error: {message}')
    else:
        print(f'rss-reader: info: {message}')


def get_project_directory_path():
    """
    This function returns path to project directory
    :return: str
    """
    return Path(getframeinfo(currentframe()).filename).resolve().parent


def create_directory(path, name):
    """
    This function creates directory
    :param path: path to directory (str)
    :param name: new directory name (str)
    :return: None
    """
    if os.path.exists(path):
        path = os.path.join(path, name)
        if not os.path.exists(path):
            os.mkdir(path)

def main():
    """
    This function parse program arguments, gets and outputs RSS news and makes logs
    :return: None
    """
    create_directory(get_project_directory_path(), data_dir_name)

    parser = argparse.ArgumentParser(description='Pure Python command-line RSS rss_reader.')
    parser.version = current_version
    parser.add_argument('source', type=str, help='RSS URL')
    parser.add_argument('--version', help='Print version info', action='version')
    parser.add_argument('--json', help='Print result as JSON in stdout', action="store_true")
    parser.add_argument('--verbose', help='Output verbose status messages', action="store_true")
    parser.add_argument('--limit', type=int, help='Limit news topics if this parameter provided', default=-1)
    parser.add_argument('--date', type=str, help='Get news by date (date format: "yyyymmdd")', default='')

    args = parser.parse_args()

    logger = logging.getLogger('rss_reader')
    logger.setLevel(logging.INFO)
    file_handler = logging.FileHandler(os.path.join(get_project_directory_path(), data_dir_name, log_file_name))
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    if args.verbose:
        stream_handler = logging.StreamHandler(sys.stdout)
        logger.addHandler(stream_handler)

    cache = caching.Cache(os.path.join(get_project_directory_path(), data_dir_name, cache_file_name))
    try:
        cache.load()
    except Exception as exc:
        logger.error(exc)

    is_error = False

    logger.info(f'Program started with URL "{args.source}"')

    if args.date:
        if news_date.is_valid_date(args.date):
            rss_news = cache.get_news(args.source, args.date, args.limit)  # try
            if not rss_news:
                is_error = True
                message = f'There is no news in cache published {args.date}'
                logger.info(message)
                if not args.verbose:
                    print_message(message)
        else:
            is_error = True
            message = f'Date {args.date} does not match format yyyymmdd'
            logger.error(message)
            if not args.verbose:
                print_message(message, is_error=True)
    else:
        rss_news = News(args.source, args.limit)
        try:
            rss_news.parse_news()
            cache.add_news(rss_news)
        except Exception as err:
            is_error = True
            error_message = err
            logger.error(error_message)
            if not args.verbose:
                print_message(error_message, is_error=True)
    if not is_error:
        if args.json:
            print_json(rss_news, 2)
            logger.info(f'{rss_news.get_count()} news were displayed in the console in json format')
        else:
            print(rss_news)
            logger.info(f'{rss_news.get_count()} news were displayed in the console')

    try:
        cache.dump()
    except Exception as exc:
        logger.error(exc)
    logger.info('Program completed')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print_message(e, is_error=True)
