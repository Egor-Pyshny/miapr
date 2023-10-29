using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Windows;
using System.Threading.Tasks;

namespace MiAPR
{
    public class NotTerminals
    {
        public string name { get; private set; }
        public Point start { get; private set; }
        public Point end { get; private set; }

        private const int delta = 10;
        /*
        a1 - vertical line
        a2 - horizontal line
        a3 - left down right top line
        a4 - left up right down line
         */
        public NotTerminals(Point start, Point end) {
            name = Classification(start, end);
            this.start = start;
            this.end = end;
        }

        private string Classification(Point start, Point end)
        {
            double delta_x = start.X - end.X; 
            double delta_y = start.Y - end.Y;
            if (Math.Abs(delta_x) < delta)
            {
                return "a1";
            }
            else if (Math.Abs(delta_y) < delta)
            {
                return "a2";
            }
            else if (start.Y > end.Y && delta_x > 50)
            {
                return "a3";
            }
            else if (start.Y > end.Y && delta_x < -50)
            {
                return "a4";
            }
            return null;
        }
    }
}
