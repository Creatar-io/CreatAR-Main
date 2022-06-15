const query = `
{
  user(username:"dibyasom") {
    publication {
      posts {
        title
        brief
        slug
        cuid
        dateUpdated
        dateAdded
        totalReactions
        replyCount
        coverImage
        contentMarkdown
      }
    }
  }
}`;
async function getData() {
  const response = await fetch("https://api.hashnode.com", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      query: query,
    }),
  });
  const body = await response.json();
  let html = "";

  console.log(body);
  var converter = new showdown.Converter();
  body.data.user.publication.posts.forEach((post) => {
    const parsed_md = converter.makeHtml(post.contentMarkdown);
    html += `<div class="col-md-4 pt-3">
                    <div class="cardblog card shadow p-4 mb-2">
                        <div class="d-flex justify-content-between">
                            <div class="d-flex flex-row align-items-center">
                                <div class="icon"> <i class="bx bxl-mailchimp"></i> </div>
                                <div class="ms-2 c-details">
                                    <h6 class="mb-0">Dibyasom Puhan</h6> 
                                </div>
                            </div>
                           
                        </div>
                        <div class="mt-3">
                            <h5 class="heading text-bold "><u>${
                              post.title
                            }</u></h5>
                            <div class="mt-4">
                                ${parsed_md}
                                <div class="mt-3"><b>Posted on</b> : <span class="text1"> ${new Date(
                                  post.dateAdded
                                )} <br> <br> <span class="text2">${
      post.totalReactions
    } Reactions </span> <span class="text2">${
      post.replyCount
    } Replies </span> </span> </div>
                            </div>
                        </div>
                    </div>
                </div>`;
  });

  document.getElementById("blog-content").innerHTML = html;
}

getData();
