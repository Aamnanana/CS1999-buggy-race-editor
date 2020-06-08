from flask import Flask, render_template, request, jsonify
import sqlite3 as sql
app = Flask(__name__)


DATABASE_FILE = "database.db"
DEFAULT_BUGGY_ID = "1"

BUGGY_RACE_SERVER_URL = "http://rhul.buggyrace.net"


#------------------------------------------------------------
# the index page
#------------------------------------------------------------
@app.route('/')
def home():
   return render_template('index.html', server_url=BUGGY_RACE_SERVER_URL)

#------------------------------------------------------------
# creating a new buggy:
#  if it's a POST request process the submitted data
#  but if it's a GET request, just show the form
#------------------------------------------------------------
@app.route('/new', methods = ['POST', 'GET'])
def create_buggy():
    con = sql.connect(DATABASE_FILE)
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("SELECT * FROM buggies")
    record = cur.fetchone(); 

    if request.method == 'GET':
        return render_template("buggy-form.html", buggy = None)
    elif request.method == 'POST':
        total_cost = ""
        msg=""
        hamster = ""

        buggy_id = request.form['id']

        flag_pattern = request.form['flag_pattern']
        msg = f"flag_pattern={flag_pattern}" 

        qty_wheels = request.form['qty_wheels']
        if not qty_wheels.isdigit():
            msg = f"{qty_wheels} is not a number. Please try again!" 
            return render_template("buggy-form.html", msg = msg, buggy = record)
        elif not int(qty_wheels) % 2 == 0:
            msg = f"{qty_wheels} is not an even number. Please try again!" 
            return render_template("buggy-form.html", msg = msg, buggy = record)
        elif int(qty_wheels) <= 2:
            msg = f"You cannot have {qty_wheels}. Please try again!" 
            return render_template("buggy-form.html", msg = msg, buggy = record)

        flag_color = request.form['flag_color']
        flag_color_secondary = request.form['flag_color_secondary']
        if flag_color.isdigit():
          msg = f"{flag_color} must be a colour! Try again." 
          return render_template("buggy-form.html", msg = msg, buggy = record)
        elif flag_color_secondary.isdigit():
          msg = f"{flag_color_secondary} must be a colour! Try again." 
          return render_template("buggy-form.html", msg = msg, buggy = record)
        
        hamster_booster = request.form['hamster_booster']
        if not hamster_booster.isdigit():
          hamster = f"Please try again. Hamster booster is a number!" 
          return render_template("buggy-form.html", hamster = hamster, buggy = record, msg = msg)
        else:
          total_cost = int(hamster_booster) * 5
          print(total_cost)
          hamster = f"Total cost of buggy is: {total_cost}" 

        try:
            with sql.connect(DATABASE_FILE) as con:
                cur = con.cursor()

                if buggy_id.isdigit():
                  cur.execute("UPDATE buggies SET qty_wheels=? WHERE id=?", (qty_wheels, buggy_id))
                else:
                  cur.execute("INSERT INTO buggies (qty_wheels) VALUES (?)", (qty_wheels,))

                # cur.execute(
                #     "UPDATE buggies SET qty_wheels=?, flag_color=?, flag_color_secondary=?, flag_pattern=?, hamster_booster=?, total_cost=? WHERE id=?",
                #     (qty_wheels, flag_color, flag_color_secondary, flag_pattern, hamster_booster, total_cost, DEFAULT_BUGGY_ID)
                # )

                con.commit()
                msg = "Record successfully saved"
        except:
            con.rollback()
            msg = "error in update operation"
        finally:
            con.close()
            return render_template("updated.html", msg = msg, hamster = hamster)

#------------------------------------------------------------
# a page for displaying the buggy
#------------------------------------------------------------
@app.route('/buggy')
def show_buggies():
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies")
  records = cur.fetchall(); 
  return render_template("buggy.html", buggies = records)

#------------------------------------------------------------
# a page for editing the buggy
#------------------------------------------------------------
@app.route('/edit/<buggy_id>')
def edit_buggy(buggy_id):
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies WHERE id=?", (buggy_id,))
  record = cur.fetchone(); 
  return render_template("buggy-form.html", buggy = record)

#------------------------------------------------------------
# get JSON from current record
#   this is still probably right, but we won't be
#   using it because we'll be dipping diectly into the
#   database
#------------------------------------------------------------
@app.route('/json')
def summary():
  con = sql.connect(DATABASE_FILE)
  con.row_factory = sql.Row
  cur = con.cursor()
  cur.execute("SELECT * FROM buggies WHERE id=? LIMIT 1", (DEFAULT_BUGGY_ID))
  return jsonify(
      {k: v for k, v in dict(zip(
        [column[0] for column in cur.description], cur.fetchone())).items()
        if (v != "" and v is not None)
      }
    )

#------------------------------------------------------------
# delete the buggy
#   don't want DELETE here, because we're anticipating
#   there always being a record to update (because the
#   student needs to change that!)
#------------------------------------------------------------
@app.route('/delete', methods = ['POST'])
def delete_buggy():
  try:
    msg = "deleting buggy"
    with sql.connect(DATABASE_FILE) as con:
      cur = con.cursor()
      cur.execute("DELETE FROM buggies")
      con.commit()
      msg = "Buggy deleted"
  except:
    con.rollback()
    msg = "error in delete operation"
  finally:
    con.close()
    return render_template("updated.html", msg = msg)


if __name__ == '__main__':
   app.run(debug = True, host="0.0.0.0")