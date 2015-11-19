/*
 * Created by SharpDevelop.
 * User: LM
 * Date: 18.11.2015
 * Time: 19:33
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;
using System.Collections.Generic;
using System.Drawing;
using System.Windows.Forms;

namespace MailPasteLauncher
{
	/// <summary>
	/// Description of MainForm.
	/// </summary>
	public partial class MainForm : ApplicationContext

	{

		private NotifyIcon niIcon;

		public int MyApp(string[] args) {

			InitializeComponent(args);
			
			return 0;

		}

		[STAThread]

		public static void Main(string[] args)

		{

			MainForm cx = new MainForm();
			cx.MyApp(args);

			Application.Run(cx);

		}

		#region Initialize Components

		public void InitializeComponent(string[] args)

		{

			this.niIcon = new System.Windows.Forms.NotifyIcon();
			System.Diagnostics.Process process = new System.Diagnostics.Process();
			System.Diagnostics.ProcessStartInfo startInfo = new System.Diagnostics.ProcessStartInfo();
			startInfo.WindowStyle = System.Diagnostics.ProcessWindowStyle.Hidden;
			startInfo.FileName = "init.cmd";
			/*string path = System.IO.Path.GetDirectoryName(Application.ExecutablePath);
			Console.WriteLine(path);*/
			string argString = "";
			if(args.Length<2){
				argString = Screen.PrimaryScreen.Bounds.Width/4+" "+Screen.PrimaryScreen.Bounds.Height/4;
			}else{
				for(int i=0; i<args.Length; i++){
					argString+=" "+args[i];
				}
			}
			startInfo.Arguments = argString;
			process.StartInfo = startInfo;
			process.Start();
			process.WaitForExit();
			Environment.Exit(0);
		}

		#endregion

		private void Exit() {

			this.niIcon.Visible = false;
			this.Dispose();
			ExitThread();// this.Close();

		}

	}
}
