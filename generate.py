import re
import json

def get_infos():
    with open('list.txt') as fin:
        lines = (line.strip() for line in fin if line.strip())

        while True:
            try:
                image = 'xxx'
                header, title, link = lines.next(), lines.next(), lines.next()
                if re.match(r'[\dA-Z]{10}', link):
                    image = '%s.jpg' % link
                    link = 'http://www.amazon.com/dp/%s/' % link

                yield header, title, link, image
            except:
                break

#with open('great_comics.txt', 'w') as fout:
#    for head, title, link, isbn in get_infos():
#        print head
#
#        fout.write(head + '\n')
#        fout.write(title + '\n')
#        fout.write(link + '\n')
#        fout.write('images/%s.jpg' % isbn + '\n\n')

with open('great_comics.json', 'w') as fout:
    items = []

    for head, title, link, image in get_infos():
        items.append(dict(
            head=head,
            title=title,
            link=link,
            image=image,
        ))

    json.dump(items, fout, indent=4)

print 'wrote great_comics.txt'
