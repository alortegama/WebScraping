from dominate.tags import *
from dominate import document
from datetime import datetime


class HtmlBuilder(object):
    def __init__(self):
        self.doc = document(title='Articles')
        with self.doc.head:
            meta(charset='UTF-8')
            link(rel="stylesheet", href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css")
        with self.doc:
            hr()
            with h1('Articles:'):
                attr(cls='text-center h1 text-primary')

    def append_data(self, data, webpage):
        with self.doc:
            hr()
            with h2(webpage):
                attr(cls='text-center h2 text-secondary')
            with div():
                attr(cls='container')
                for article in data:
                    with div():
                        attr(cls='card mb-3')
                        with div():
                            attr(cls='row g-0')
                            with div():
                                attr(cls='col-md-4')
                                with img():
                                    attr(cls='img-fluid rounded-start', src=article.image)
                            with div():
                                attr(cls='col-md-8 d-flex flex-column justify-content-between')
                                with div():
                                    attr(cls='card-body')
                                    with h5(article.title):
                                        attr(cls='card-title')
                                    with p(article.resume):
                                        attr(cls='card-text')
                                    with p():
                                        with a('Read more...'):
                                            attr(cls='card-link', href=article.url)
                                    with p():
                                        date = datetime.strptime(article.time, '%Y-%m-%dT%H:%M:%SZ')
                                        with small(
                                                f'Published at: {str(date.strftime("%H"))}:{str(date.strftime("%M"))}'):
                                            attr(cls='text-muted')

                                with div():
                                    with blockquote():
                                        attr(cls='blockquote mb-auto text-center')
                                        with footer(article.author):
                                            attr(cls='blockquote-footer')

    def write_html(self):
        with open('articles.html', 'w') as f:
            f.write(self.doc.render())
