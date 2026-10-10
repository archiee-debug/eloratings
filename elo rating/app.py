from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        ra = int(request.form.get("ra", 1000))
        rb = int(request.form.get("rb", 1000))
        sa = float(request.form.get("result", 0.5))

        k = 32

        ea = 1 / (1 + 10 ** ((rb - ra) / 400))
        eb = 1 / (1 + 10 ** ((ra - rb) / 400))

        new_ra = ra + k * (sa - ea)
        new_rb = rb + k * ((1 - sa) - eb)

        return render_template(
            "index.html",
            new_ra=round(new_ra, 2),
            new_rb=round(new_rb, 2)
        )

    # Return a response for GET requests too
    return render_template(
        "index.html",
        new_ra=None,
        new_rb=None
    )

if __name__ == "__main__":
    app.run(debug=True)