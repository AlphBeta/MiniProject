import java.awt.*;
import java.awt.event.*;
import java.text.*;
import java.util.*;
import javax.swing.*;

public class MyFrame extends JFrame{
 
 SimpleDateFormat timeFormat;
 SimpleDateFormat dayFormat;
 SimpleDateFormat dateFormat;
 JLabel timeLabel;
 JLabel dayLabel;
 JLabel dateLabel;
 JLabel placeLabel;
 String time;
 String day;
 String date;
 //Scanner sc = new Scanner(System.in);
 MyFrame(String s){
  /*System.out.print("Continent:");
  String s1=sc.nextLine();
  System.out.print("Capital/Place:");
  String s2=sc.nextLine();
  String s=s1+"/"+s2;*/
  this.setLayout(new FlowLayout());
  this.setSize(500,500);
  this.setResizable(false);
  this.setVisible(true);

  this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  this.setTitle("World Clock");
  timeFormat = new SimpleDateFormat("hh:mm:ss a");
  dayFormat = new SimpleDateFormat("EEEE");
  dateFormat = new SimpleDateFormat("MMMMM dd, yyyy");
  
  timeLabel = new JLabel();
  timeLabel.setFont(new Font("Verdana",Font.PLAIN,55));
  timeLabel.setForeground(new Color(0x00ffff));
  timeLabel.setBackground(Color.black);
  timeLabel.setOpaque(true);
  
  dayLabel = new JLabel();
  dayLabel.setFont(new Font("Ink Free",Font.PLAIN,35));
  
  dateLabel = new JLabel();
  dateLabel.setFont(new Font("Ink Free",Font.PLAIN,30));

  placeLabel=new JLabel(s);
  placeLabel.setFont(new Font("Courier New",Font.PLAIN,40));

  this.add(timeLabel);
  this.add(dayLabel);
  this.add(dateLabel);
  this.add(placeLabel);
  setTime(s);
 }

 public void setTime(String t) {
  while(true) {
  Date today = new Date();
  timeFormat.setTimeZone(TimeZone.getTimeZone(t));
  dayFormat.setTimeZone(TimeZone.getTimeZone(t));
  dateFormat.setTimeZone(TimeZone.getTimeZone(t));
  
  time = timeFormat.format(today);
  timeLabel.setText(time);

  day = dayFormat.format(today);
  dayLabel.setText(day);
  
  date = dateFormat.format(today);
  dateLabel.setText(date);
  
  try {
   Thread.sleep(1000);
  } catch (InterruptedException e) {
   // TODO Auto-generated catch block
   e.printStackTrace();
  }
  }
 }
}